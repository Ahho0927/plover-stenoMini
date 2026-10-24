"""받침 조건에 따른 문자열 선택. 표준 라이브러리만 사용합니다."""

import unicodedata

_BATCHIM = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"


def select_batchim_text(previous_text, without_batchim, with_batchim, exception=None):
    """끝 한글의 받침을 판단합니다. 판단 불가 시 받침 있는 출력을 선택합니다."""
    text = unicodedata.normalize("NFC", previous_text.rstrip())
    if not text or not "가" <= text[-1] <= "힣":
        return with_batchim
    index = (ord(text[-1]) - ord("가")) % 28
    if index == 0 or _BATCHIM[index - 1] == exception:
        return without_batchim
    return with_batchim


def ko_batchim_condition(context, argument):
    """{:ko_batchim_condition:받침없음,받침있음[,예외받침]}"""
    parts = argument.split(",")
    if len(parts) not in (2, 3):
        raise ValueError(
            "ko_batchim_condition requires: without_batchim,with_batchim[,exception]"
        )
    without_batchim, with_batchim = parts[:2]
    exception = parts[2] if len(parts) == 3 and parts[2] else None
    if exception is not None and (len(exception) != 1 or exception not in _BATCHIM):
        raise ValueError("ko_batchim_condition exception must be one Korean batchim")
    previous_word = "".join(context.last_words(1)).rstrip()
    selected = select_batchim_text(
        previous_word, without_batchim, with_batchim, exception
    )
    # 앞에 붙이되 기존 출력을 다시 쓰지 않아 명시적 공백을 보존합니다.
    action = context.new_action()
    action.prev_attach = True
    action.next_attach = False
    action.text = selected
    words = (previous_word + selected).split()
    action.word = words[-1] if words else None
    return action
