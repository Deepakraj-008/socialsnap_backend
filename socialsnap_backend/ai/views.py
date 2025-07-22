import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from .models import AIInteraction
from .serializers import AIInteractionSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ai_chat(request):
    input_text = request.data.get("message", "")
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": input_text}]
            }
        )
        response.raise_for_status()
        ai_response = response.json()["choices"][0]["message"]["content"]
        
        interaction = AIInteraction.objects.create(
            user=request.user,
            input_text=input_text,
            response=ai_response
        )
        
        return Response({"response": ai_response})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

