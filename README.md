## openCV_legoSize
openCV를 이용해서 LEGO 빔의 사이즈를 체킹 하는 프로그램이다. </br>
물론 LEGO 말고도 다른것도 가능하다. 가급적 각이진 물건이 가장 좋다.</br>
하지만 단점이 있다면 이 코드는 아직 까진 실시간으로 인식이 되질 않는다. 실시간 코드를 현재 작성 중이긴 하지만 꽤 오래 걸릴거 같다. </br>

## Before the Starting...
🗣이 코드는 Adrian Rosebrock의 코드을 이용하여 작성 되었습니다.
[<a href="https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/">참고 사이트</a>]🗣 </br>
Thank you Adrian! :)

## Requirements
<ul>
  <li><a href="www.python.org">[Python]</a></li>
  <li><a href="www.opencv.org">[openCV]</a></li>
  <li>[Webcam]</li>
</ul>

## Prepare to RUN 

작성일 2018년 3월 기준으로 현재는 맥과 리눅스에서 테스트를 해봤을때 문제 없이 잘 되었다. </br>
아직 까진 윈도우에 대해서는 잘 모르겠지만 윈도우도 잘 되지 않을까 싶다. </br> 

</br>

프로그램을 위해서 먼저 컴퓨터에 openCV가 설치가 되 있어야 한다. </br>
openCV는 Windows, Mac, Linux 마다 다 설치 방법이 다르다. 혹시 몰라 설치 방법을 아래 링크에 넣어두었다. </br>
[👉<a href="https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html">"Windows"</a>👈] </br>
[👉<a href="https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/">"Mac"</a>👈]</br>
[👉<a href="https://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/">"Linux"</a>👈]</br>
</br>
이 프로그램이 테스트된 컴퓨터의 사양은 다음과 같다.
<pre>
Hardware :
Macbook Pro(Retina, 13-inch, Early 2015
2.7GHz Intel Core i5
8 GB 1867 MHz DDR3
Intel Iris Graphics 6100 1536 MB

Software :
macOS High Sierra Version '10.13.3'
Python '2.7.14'
openCV Version '3.4.0'
Linux Ubuntu '16.04.4'
Edit Tool Visual Stuido Code '1.23.0'
</pre>
~~일종의 컴퓨터 자랑이다, 헣~~. 사실 프로그래머가 맥 유저여서 윈도우를 그닥 쓰질 않는다. 혹시 윈도우로 테스트 하고 버그가 생긴다면 말해주길 바란다. 딱히 이상한 의도는 전혀 없다. 그저 포스팅을 위해서 말하는 것이다. </br>
</br>
openCV 설치를 다했다면 이제 pip 설치를 해야한다. 설치해야 할 패키지가 생각보다 많다. </br>
아래에 pip 설치 명령어를 입력 했다. 자신이 마우스를 잘 쓴다면 마우스로 Copy -> Paste 를 이용하거나 Ctrl + C -> Ctrl + V 를 이용하길 바란다.</br>
<pre>
~ $ pip install argparse
~ $ pip install imutils
~ $ pip install logging
~ $ pip install datetime
~ $ pip install csv
</pre>

## openCV Measuring Size Image 
openCV를 실행을 하기전에 터미널에서 실행을 해봐야 한다. </br>
<pre>
$ python 
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'3.4.0'
>>>
</pre>
이게 된다면 괜찮은거 같다. 카메라 실시간 인식 코드는 현재 작성중이다. 작성이 끝나면 이 저장소에다가 올릴 예정이다. </br>
실행을 하기전에 먼저 사진이 있어야 한다. 일단 테스트 사진은 이거다. </br>
![test1](https://github.com/insung3511/openCV_legoSize/blob/master/openCV_Size/openCV-image/images/test1.JPG)
</br>
실행 명령어는 다음과 같다. 
<pre>
$ python openCV_Size.py -i .../images/test1.JPG -w 3.5
</pre>
그 실행에 대한 결과는 다음 GIF와 나온다. </br>
<p align="center">
<img align="center" src="https://github.com/insung3511/openCV_legoSize/blob/master/Example-1.gif" width= "100%" alt="Example File "test1.JPG" "/>
</p>

현재 코드가 LEGO Bean에 기준으로 작성이 되어서 터미널에는 어떤 빔이 인식이 되었다고 나올수도 있다. </br>
기존 코드의 좌표는 위에 하이퍼링크로 걸어 놓았다. </br>

## openCV Measuring Size Real-Time
완전 실시간 인식 시스템은 아니다만, 그래도 나름 **비슷** 하게 만들었다. 이것 또한 어디까지나 목표를 위해서 거치는 과정 중 하나라고 생각하면 된다. </br>
실행 방법은 간단하지만, 그 속은 전혀 간단하지 않다. 

## Contact me
If you have problem about this code, then contect me. </br>
Email : insung.park123@gmail.com </br>
Facebook : https://www.facebook.com/insung.bahk </br>
</br>
If you want to give me some money... Please money send here! </br>
Bitcoin : 17qKUu57aUBcvx9T1ea8Ga87EPnDdmwAEP </br>
Ether : 0xdFE8D1536deE8F839Ede7c1f3A0c44116287D931  
Bitcoin Cash : qp90gf09r3y3h06czmtnsfhz9w7s90se4s72vd9pam </br> 
</br>
🙇‍♀️👾🤩Thank you! 🤩👾🙇‍♂️ 
