def solution(numbers, target):
    answer = 0

    def dfs(idx, operated):
        nonlocal answer
        if idx < len(numbers):
            number = numbers[idx]
            dfs(idx+1, operated + number)
            dfs(idx+1, operated - number)
            return
        else:
            if operated == target:
                answer += 1

    dfs(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))


/*
    dfs(0,0){
        dfs(1,1){   // +1
            dfs(2,2) {  // +1+1
                dfs(3,3){   // +1+1+1
                    dfs(4,4){   // +1+1+1+1
                        dfs(5,5){   // +1+1+1+1+1
                            return false
                        }
                        dfs(5,3){   // +1+1+1+1-1
                            answer += 1
                        }
                    }
                    dfs(4,2){   // +1+1+1-1
                        dfs(5,3){   // +1+1+1-1+1
                            answer += 1
                        }
                        dfs(5,1){   // +1+1+1-1-1
                            return
                        }
                    }
                }
                dfs(3,1){   // +1+1-1
                    dfs(4,2){   // +1+1-1+1
                        dfs(5,3){   // +1+1-1+1+1
                            answer += 1
                        }
                        dfs(5,1){   // +1+1-1+1-1
                            return
                        }
                    }
                    dfs(4,0){   // +1+1-1-1
                    }
                }
            }
            dfs(2,0) {
                dfs(3,1){

                }
                dfs(3,-1){
                }
            }
        }
        dfs(1,-1)
    }
*/