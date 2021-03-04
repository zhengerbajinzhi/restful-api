from django.shortcuts import render

# Create your views here.

from demo.models import IpPool
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.views import APIView


class Pool(APIView):  # 这里必须继承APIView，否则不会生效
    throttle_scope = 'test'  # 这里对接口进行限制，匿名用户和登录用户是全局生效的，不用管

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Pool, self).dispatch(*args, **kwargs)

    def get(self, request, id=0):
        search_dict = {}
        # 获取GET传值参数
        agreement = request.GET.get('agreement')
        ip_address = request.GET.get('ip_address')
        # 如果存在参数，则添加到搜索条件
        if id:
            search_dict['id'] = id
        if agreement:
            search_dict['agreement'] = agreement
        if ip_address:
            search_dict['ip_address'] = ip_address
        # 根据搜索条件查询结果
        pools = IpPool.objects.filter(**search_dict)
        result = []
        for p in pools:
            ip_info = {
                'agreement': p.agreement,
                'ip_address': p.ip_address,
            }
            result.append(ip_info)
        # 返回用户信息列表
        return JsonResponse({'code': 0, 'message': 'Success!', 'data': result})

    def post(self, request):
        agreement = request.POST.get('agreement', '')
        ip_address = request.POST.get('ip_address', '')
        if ip_address != '':
            ip_info = {
                'agreement': agreement,
                'ip_address': ip_address
            }
            IpPool.objects.create(**ip_info)
            return JsonResponse({'code': 0, 'message': 'Success!'})
        else:
            return JsonResponse({'code': -1, 'message': 'fail! Please check your parameters.'})

    def put(self, request, id):
        update_dict = {}
        agreement = request.POST.get('agreement')
        ip_address = request.POST.get('ip_address')
        if agreement:
            update_dict['agreement'] = agreement
        if ip_address:
            update_dict['ip_address'] = ip_address

        IpPool.objects.filter(id=id).update(**update_dict)
        return JsonResponse({'code': 0, 'message': 'Success!'})

    def delete(self, request, id):
        IpPool.objects.filter(id=id).delete()
        return JsonResponse({'code': 0, 'message': 'Success!'})
