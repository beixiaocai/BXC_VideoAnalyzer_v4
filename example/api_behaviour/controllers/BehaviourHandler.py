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
                'keypoints': '315,429,310,423,311,423,290,427,310,426,276,456,319,450,267,491,338,475,276,503,340,479,290,519,317,517,305,566,320,564,307,609,315,607,',
                'keypoints_count': 17,
                'class_score': 0.64599609375,
                'class_id': 0,
                'class_name': 'person',
                'track_id': 0,
                'x1': 260,
                'x2': 354,
                'y1': 406,
                'y2': 632
            }, {
                'keypoints': '315,429,310,423,311,423,290,427,310,426,276,456,319,450,267,491,338,475,276,503,340,479,290,519,317,517,305,566,320,564,307,609,315,607,',
                'keypoints_count': 17,
                'class_score': 0.64599609375,
                'class_id': 0,
                'class_name': 'person',
                'track_id': 0,
                'x1': 260,
                'x2': 354,
                'y1': 406,
                'y2': 632
            }],
            'video_channels': 3,
            'video_fps': 30,
            'video_height': 1080,
            'video_width': 1920,
            'start_timestamp': 1701506101680,
            'check_fps': 20,
            'frame_count': 442,      
            'polygon': '0.0000,0.0000,1.0000,0.0000,1.0000,1.0000,0.0000,1.0000',
            'polygon_type': 0,
            'overlap_thresh': 0.5,
            'min_minterval': 0.5
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
