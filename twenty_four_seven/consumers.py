import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from twenty_four_seven.models import *


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'twenty_four_seven'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def change_item_status(self, item_id):
        item = Item.objects.get(pk=item_id)
        item.in_work = True
        item.save()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        item_id = text_data_json['item_id']

        self.change_item_status(item_id)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'project_message',
                'message': message
            }
        )
    
    def project_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'update': {
                'post_id':'post_id',
                'status': 'status',
            }
        }))
