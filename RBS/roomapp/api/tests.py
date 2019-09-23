from rest_framework.test import APITestCase

from roomapp.models import book_room
# Create your tests here.
class booking_ApiTestcase(APITestCase):
    def setup(self):
        book_room.objects.create(username='swamy',
                                 room='r1',
                                 booked_date='2019-9-2',
                                 to_date='2019-9-11',
                                 room_book='room_booked'
                                 )

    def test_post_metod(self):
        url='http://127.0.0.1:8000/roomapp/book/'
        data={
               'username':'swamy',
               'room':'r1',
               'booked_date':'2019-9-2',
               'to_date' : '2019-9-11',
                'room_book' :'room_booked'
           }
        response=self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code,201)

