# plover-stenoMini

stenoMini의 26개 논리 키와 기본 한글 사전, 받침 조건 메타를 제공하는 Plover 플러그인입니다.

## 구성

- `pyproject.toml`: 배포 이름 `plover-stenoMini`, System 이름 `stenoMini`, 메타 이름 `ko_batchim_condition`을 등록함.
- `plover_stenoMini/system.py`: 논리 키 순서, Keyboard 매핑, 기본 사전 경로.
- `plover_stenoMini/meta.py`: 한글 유니코드로 받침을 계산하는 메타.
- `plover_stenoMini/dictionaries/stenoMini_hangul.json`: 기본 한글 사전.
- `plover_stenoMini/dictionaries/stenoMini_brief.json`: 기본 약어 사전.

## 설치 및 업데이트 (macOS)

Plover를 종료하고 이 README가 있는 `plover-stenoMini` 폴더에서 실행하세요.

```bash
PYTHONUSERBASE="$HOME/Library/Application Support/plover/plugins/mac" \
"/Applications/Plover.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3" \
-m plover.plugins_manager install --no-build-isolation .
```

Plover 재실행 후 Configure → System → **stenoMini**를 선택하세요.
일반 키보드는 Machine을 Keyboard로 설정하세요.
전용 속기 장치는 해당 Machine용 키 매핑이 별도로 필요합니다.

## 사전에 대해

### 받침 조건 메타

사전 값에 다음과 같이 사용합니다. 다른 System에서도 사용할 수 있습니다.

```text
{^}{:ko_batchim_condition:는,은,를}
{^}{:ko_batchim_condition:를,을,를}
```

인수는 **받침 없는 경우, 받침 있는 경우, 예외 받침(선택)** 순서입니다.
`학교` + 첫 번째 메타 → `학교는`, `학생` + 첫 번째 메타 → `학생은`.
`학교`/`학생`/`%` + 두 번째 메타 → `학교를`/`학생을`/`%를`.
앞에 자동으로 붙고, 다음 출력은 기본 띄어쓰기 규칙을 따릅니다.

인수 내부의 공백은 보존합니다. 쉼표는 인수 구분자입니다.
인수 안의 Plover 명령은 해석하지 않습니다. 명령은 메타 뒤에 작성하세요.
마지막 단어의 끝 글자를 판단하며 뒤쪽 공백은 판단할 때 제외합니다.
분해된 한글은 NFC로 정규화합니다. 끝 글자가 한글 음절이 아니거나 이전 출력이 없으면 받침 있는 경우를 선택합니다.
영문/숫자의 발음 또는 문장부호 앞의 받침을 추정하지 않습니다.
잘못된 인수 개수 또는 예외 받침은 오류로 처리합니다.

### 사전 수정 및 폴더 이름

첫 활성화 시 기본 사전이 `~/Library/Application Support/plover/stenoMini_base.json`으로 복사됩니다.
실사용 사전은 그 복사본이며 재설치로 기존 복사본을 덮어쓰지 않습니다.
Plover 사전 편집기 또는 Add Translation으로 실사용 사전을 수정하세요.
