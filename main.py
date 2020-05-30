import MildomCommentViewer
import sys

room_id = sys.argv[1]

mcv = MildomCommentViewer.MildomCommentViewer(room_id)
mcv.start()
