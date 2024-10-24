# exceptions.py

from rest_framework.views import exception_handler

def baseExceptionHandler(exc, context):
    # 调用 DRF 的默认异常处理器获取标准响应
    response = exception_handler(exc, context)
    print(exc,context)
    # 如果响应为 None，意味着异常未被 DRF 捕获
    if response is None:
        return {
            'code': 4002,
            'msg': str(exc),
            'data': None
        }

    # 自定义响应格式
    response_data = {
        'code': 4004,
        'msg': response.data.get('detail', '发生错误'),  # 你可以根据需要修改消息
        'data': None
    }

    response.data = response_data
    return response
