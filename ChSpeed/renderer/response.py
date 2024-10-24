from rest_framework.renderers import JSONRenderer
class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # 封装信息
        if isinstance(data, dict):
            msg = data.pop('msg', '操作成功')
            err_code = data.pop('code',0)
        else:
            msg = '操作成功'
            err_code = 0
        ret={'data':data,'code':err_code,'msg':msg}
        return super().render(ret, accepted_media_type, renderer_context)
