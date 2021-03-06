# -*- coding: utf8 -*-
# Xử lý Tiếng Việt trong python
import pygst
pygst.require("0.10")
import gst

def on_tag(bus, msg):
    taglist = msg.parse_tag()
    print 'on_tag:'
    for key in taglist.keys():
        print '\t%s = %s' % (key, taglist[key])

#our stream to play

# URL chứa file audio
music_stream_uri='http://download.s82.stream.nixcdn.com/476334538857f6725d4ec295a57713c3/56fd1387/NhacCuaTui881/NeuKhongTheDenVoiNhau-TrinhDinhQuang-3696978.mp3'

#creates a playbin (plays media form an uri)
player = gst.element_factory_make("playbin", "player")

#set the uri
player.set_property('uri', music_stream_uri)

#start playing
player.set_state(gst.STATE_PLAYING)

#listen for tags on the message bus; tag event might be called more than once
bus = player.get_bus()
bus.enable_sync_message_emission()
bus.add_signal_watch()
bus.connect('message::tag', on_tag)

#wait and let the music play
raw_input('Nhấn phím bất kỳ để tạm dừng...')