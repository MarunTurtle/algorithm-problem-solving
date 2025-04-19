def solution(expressions):
    # 주어진 진법 식 리스트에서 X(미지수)가 있는 식의 결과를 채워 문자열 리스트로 반환하는 함수

    def is_valid_digit(num_str, base):
        # num_str의 각 문자가 base 미만의 숫자인지 확인
        return all(int(ch) < base for ch in num_str)

    def is_valid(expr, base):
        # base 진법에서 expr 식이 올바른지 (연산 결과가 맞는지) 확인
        try:
            a, op, b, _, c = expr.split()  # "a op b = c" 형태 분해
            # 피연산자와 결과(c)가 해당 진법에서 사용 가능한 숫자인지 검사
            if not (is_valid_digit(a, base) and is_valid_digit(b, base) and is_valid_digit(c, base)):
                return False
            # 진법 변환하여 정수로 계산
            a_base = int(a, base)
            b_base = int(b, base)
            c_base = int(c, base)
            # 덧셈 또는 뺄셈 결과 비교
            if op == '+':
                return a_base + b_base == c_base
            else:
                return a_base - b_base == c_base
        except:
            return False

    def evaluate_expr(a, op, b, base):
        # base 진법에서 "a op b" 계산 후 결과를 문자열로 반환 (불가능 시 None)
        # 피연산자가 해당 진법에 유효한지 확인
        if not (is_valid_digit(a, base) and is_valid_digit(b, base)):
            return None
        a_base = int(a, base)
        b_base = int(b, base)
        # 덧셈 또는 뺄셈 수행
        result = a_base + b_base if op == '+' else a_base - b_base
        if result < 0:
            return None
        # 결과가 0일 때
        if result == 0:
            return "0"
        # 결과를 base 진법 문자열로 변환
        digits = ""
        while result > 0:
            digits = str(result % base) + digits
            result //= base
        return digits

    # X가 없는 식(known)과 X가 있는 식(unknown) 분리
    known   = [e for e in expressions if 'X' not in e]
    unknown = [e for e in expressions if 'X'     in e]

    # 1) 가능한 진법 후보 찾기 (2진법부터 9진법까지)
    valid_bases = []
    for base in range(2, 10):
        # a) known 식들이 모두 성립하는지 확인
        if not all(is_valid(expr, base) for expr in known):
            continue

        # b) 모든 표현식의 숫자가 해당 진법에서 유효한지 검사
        legal = True
        for expr in expressions:
            a, op, b, _, c = expr.split()
            for num_str in (a, b, c):
                if num_str == 'X':
                    continue
                if not is_valid_digit(num_str, base):
                    legal = False
                    break
            if not legal:
                break

        if legal:
            valid_bases.append(base)

    # 2) unknown 식들에 대해 결과 채우기
    results = []
    for expr in unknown:
        a, op, b, _, _ = expr.split()
        # 각 후보 진법에서 계산 가능한 결과 모음
        possible = {
            evaluate_expr(a, op, b, base)
            for base in valid_bases
            if evaluate_expr(a, op, b, base) is not None
        }
        # 결과가 한 가지이면 해당 값으로, 아니면 물음표
        if len(possible) == 1:
            val = possible.pop()
            results.append(f"{a} {op} {b} = {val}")
        else:
            results.append(f"{a} {op} {b} = ?")

    return results