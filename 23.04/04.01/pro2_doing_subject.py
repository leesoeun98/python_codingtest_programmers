# 1차 실패 - 40분 소요 => 로직에서 plans 도는 과정에서 stack 동시 접근해야 함을 놓침 (문제 이해를 잘 못함)
# 2차 실패 - 1시간 20분 소요
# 3차 실패 - 8분 소요 (계속 58.3점)
# 4차 시도 - 32분 소요, 다른 사람 풀이 봄
# 틀린 이유 :
# 1. stack 쓰는건 알았는데 구현력이 약함.
# 2. 너무 복잡하게 생각함
# 3. date같은 형식에 집착하지 말고 여기서 startTime은 stack에 넣는 순간 볼 필요 없으므로 stamp 같이 쉽게 변형하자

stack, answer = [], []


def solution(plans):
    # 배열을 시작 시간 순으로 정렬
    plans.sort(key=lambda x: x[1])
    # 배열의 item중 playing time을 int로 변환
    plans = list(map(lambda x: [x[0], x[1], int(x[2])], plans))

    for item in plans:
        cur_leftTime = item[2]
        # 시간은 모두 timestamp로 바꾸자
        hour, min = map(int, item[1].split(':'))
        cur_stampTime = 60*hour + min

        if stack:
            prev_subject, prev_startStampTime, prev_leftTime = stack.pop()
            # 여유 시간 (새로운 과제 시작 시간 - 이전 과제 시작 시간)
            leftTime = cur_stampTime - prev_startStampTime

            # leftTime이랑 prev_leftTime을 비교
            # 1. leftTime이 더 크거나 같으면, 과제는 멈추지 않고 한 번에 끝남 (answer, leftTime 갱신 필수)
            # => 과제 끝나고 나서 stack을 처리 할지, 다음 과제를 바로 처리할 지 판단해야 함
            if prev_leftTime <= leftTime:
                answer.append(prev_subject)
                leftTime -= prev_leftTime

                # 1. leftTime이 0이고 stack도 비어있으면 바로 다음 과제 (즉, stack 처리 부분 빠져 나옴)
                # 2. leftTime도 남아있고, stack에도 뭔가가 남아 있으면 멈춘 과제 먼저 해결
                while stack and leftTime:
                    prev_subject, prev_startStampTime, prev_leftTime = stack.pop()
                    # stack 처리 중 더 이상 leftTime이 prev_leftTime 보다 작아서,
                    # 과제를 한번에 끝낼 수 없으면 stack 추가 후 종료
                    if leftTime < prev_leftTime:
                        stack.append([prev_subject, prev_startStampTime, prev_leftTime - leftTime])
                        break
                    # stack 처리 중 과제 한 번에 끝날 수 있으면 answer, leftTime 갱신
                    else:
                        answer.append(prev_subject)
                        leftTime -= prev_leftTime

            # 2. leftTime이 더 작으면, 과제는 중간에 멈춤 (stack에 넣어야 함)
            else:
                stack.append([prev_subject, prev_startStampTime, prev_leftTime - leftTime])

        # 멈춘 과제가 없으면 일단 stack에 넣어놓고 시작하자!
        stack.append([item[0], cur_stampTime, cur_leftTime])

    return answer + list(map(lambda x: x[0], reversed(stack)))
