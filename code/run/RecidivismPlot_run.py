
# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 패키지 임포트 시 코드가 실행되는 점을 활용해 run 코드 작성
from DataVisualization.RecidivismPlot import *