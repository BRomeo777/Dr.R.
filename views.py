# dr_r_app/views.py
import os
import sys
import json
import logging
import traceback

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# -------------------------
# Import your AI agent
# -------------------------
try:
    from dr_r_agent import DrRLAgent
    logger.info("✅ DrRLAgent imported successfully")
    AGENT_AVAILABLE = True
except Exception as e:
    logger.error(f"❌ Failed to import DrRLAgent: {e}")
    DrRLAgent = None
    AGENT_AVAILABLE = False

# -------------------------
# Views
# -------------------------

def index(request):
    """Render the main page"""
    return render(request, 'dr_r_app/index.html')


def health(request):
    """Health check endpoint"""
    return JsonResponse({
        'success': True,
        'status': 'healthy',
        'agent_available': AGENT_AVAILABLE,
        'groq_key_set': bool(os.environ.get('GROQ_API_KEY'))
    })


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def search(request):
    """Search endpoint"""
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        response = JsonResponse({'success': True})
        _add_cors_headers(response)
        return response

    if not AGENT_AVAILABLE:
        response = JsonResponse({
            'success': False,
            'error': 'Search agent not available. Check server logs.'
        }, status=500)
        _add_cors_headers(response)
        return response

    try:
        if request.content_type != 'application/json':
            response = JsonResponse({
                'success': False,
                'error': 'Content-Type must be application/json'
            }, status=400)
            _add_cors_headers(response)
            return response

        data = json.loads(request.body)
        query = data.get('query', '').strip()
        max_results = data.get('max_results', 20)

        if not query:
            response = JsonResponse({
                'success': False,
                'error': 'Query cannot be empty'
            }, status=400)
            _add_cors_headers(response)
            return response

        logger.info(f"Searching for: {query}")

        try:
            agent = DrRLAgent()
            results = agent.search(query, max_results=max_results)
        except Exception as e:
            logger.error(f"Agent error: {e}")
            response = JsonResponse({
                'success': False,
                'error': 'Search failed',
                'details': str(e)
            }, status=500)
            _add_cors_headers(response)
            return response

        response = JsonResponse({
            'success': True,
            'results_count': len(results),
            'results': results
        })
        _add_cors_headers(response)
        return response

    except Exception as e:
        logger.error(f"Search endpoint error: {e}")
        logger.error(traceback.format_exc())
        response = JsonResponse({
            'success': False,
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)
        _add_cors_headers(response)
        return response

# -------------------------
# CORS helper
# -------------------------
def _add_cors_headers(response: HttpResponse):
    """Add CORS headers to the response"""
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE,OPTIONS"
    return response
