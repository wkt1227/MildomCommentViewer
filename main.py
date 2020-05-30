import MildomCommentViewer
import sys

roomId = sys.argv[1]

mcv = MildomCommentViewer.MildomCommentViewer(roomId)
mcv.start()