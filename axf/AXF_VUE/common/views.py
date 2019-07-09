import logging

from django.contrib import messages
from django.shortcuts import render


def index(request):

    # request.session.flush()

    # messages.warning(request, "用户凉了")

    logger = logging.getLogger("django")

    logger.error("这是在项目中")

    data = {
        # "info": request.session.get("info") or ""
        "messages": messages.get_messages(request)
    }

    return render(request,"index.html", context=data)
