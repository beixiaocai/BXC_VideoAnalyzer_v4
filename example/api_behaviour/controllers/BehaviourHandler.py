from controllers.BaseHandler import BaseHandler
import json


class BehaviourHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        data = await self.do()
        self.response_json(data)

    async def do(self):
        request_params = self.request_post_params()

        """
        {
            'check_fps': 20.947629928588867,
            'detects': [{
                'class_name': 'person',
                'keypoints': '315,429,310,423,311,423,290,427,310,426,276,456,319,450,267,491,338,475,276,503,340,479,290,519,317,517,305,566,320,564,307,609,315,607,',
                'keypoints_count': 17,
                'score': 0.64599609375,
                'x1': 260,
                'x2': 354,
                'y1': 406,
                'y2': 632
            }, {
                'class_name': 'person',
                'keypoints': '1735,827,1741,822,1731,820,1746,819,1717,813,1740,842,1695,831,1735,881,1656,859,1731,908,1651,893,1711,922,1683,918,1699,992,1674,988,1687,1049,1662,1046,',
                'keypoints_count': 17,
                'score': 0.591796875,
                'x1': 1635,
                'x2': 1758,
                'y1': 783,
                'y2': 1074
            }],
            'frame_count': 442,
            'overlap_thresh': 0.5,
            'recognition_region': '0.0000,0.0000,1.0000,0.0000,1.0000,1.0000,0.0000,1.0000',
            'start_timestamp': 1701506101680,
            'video_channels': 3,
            'video_fps': 30,
            'video_height': 1080,
            'video_width': 1920
        }
        """
        print(request_params)

        detects = request_params.get("detects")
        if detects:
            indices = list(range(min(len(detects),3))) # 模拟只取前三个目标的序号
        else:
            indices = []

        happen = True
        happenScore = 0.97

        result = {
            "happen": happen,
            "happenScore": happenScore,
            "indices": indices
        }
        res = {
            "code": 1000,
            "msg": "success",
            "result": result
        }
        return res
