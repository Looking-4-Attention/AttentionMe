## 사용법

아래는 간단한 예제입니다. 더 자세한 사항은 저희 Organization 내 Sample Usage repository를 참고하시기 바랍니다. 아래는 배경 제거 기능을 시작하는 코드입니다:
```python
from attentionme import *

image_path = 'sample_images/group1.jpg'
output_path = 'image_outputs/removed_background_image.png'

remove_background(image_path, output_path)
```
