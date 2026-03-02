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
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------
# Import your AI agent
# -------------------------
try:
    # Since everything is in the root, we import directly
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
    # FIX: Changed 'dr_r_app/index.html' to just 'index.html' 
    # because you don't have a dr_r_app folder.
    return render(request, 'index.html')


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
    """Search endpoint for Gastric Cancer queries"""
    if request.method == 'OPTIONS':
        response = JsonResponse({'success': True})
        _add_cors_headers(response)
        return response

    if not AGENT_AVAILABLE:
        response = JsonResponse({
            'success': False,
            'error': 'Search agent not available.'
        }, status=500)
        _add_cors_headers(response)
        return response

    try:
        data = json.loads(request.body)
        query = data.get('query', '').strip()
        max_results = data.get('max_results', 20)

        if not query:
            return _error_response('Query cannot be empty', 400)

        logger.info(f"Searching Gastric Cancer data for: {query}")

        agent = DrRLAgent()
        # Ensure your DrRLAgent class has a search method
        results = agent.search(query, max_results=max_results)

        response = JsonResponse({
            'success': True,
            'results_count': len(results),
            'results': results
        })
        _add_cors_headers(response)
        return response

    except Exception as e:
        logger.error(f"Search error: {e}")
        return _error_response(str(e), 500)

def _error_response(message, status_code):
    response = JsonResponse({'success': False, 'error': message}, status=status_code)
    return _add_cors_headers(response)

def _add_cors_headers(response: HttpResponse):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response
