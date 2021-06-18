# 전방 탐색

# 긍정형 전방 탐색을 이용하여 com, net 만 매칭시키겠다.
import re
p = re.compile(r".*[@].*[.](?=com$|net$).*$")