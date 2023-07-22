import sys
input = sys.stdin.readline
print = sys.stdout.write

def setStar(A, n, row, col):
    """
    matrix A에서 n 크기의 삼각형 만들 때,
    row,col을 중심으로 하는 삼각형을 그려준다.
    """
    if n == 3:
        setBasicStar(row, col,A)
    else:
        next_n = n//2
        # 3개 삼각형의 상대 좌표
        next_1 = (0, 0)
        next_2 = (n//2, n//2)
        next_3 = (n//2, -n//2)
        setStar(A, next_n, row+next_1[0], col+next_1[1])
        setStar(A, next_n, row+next_2[0], col+next_2[1])
        setStar(A, next_n, row+next_3[0], col+next_3[1])


def setBasicStar(n,m, matrix):
    """
    n,m를 start로 하는 n=3 짜리 기본 별을 배열에 넣는다.
    별 : '*'
    n,m을 시작지점이라고 할 때, (시작지점은 첫번째줄 가운데 꼭지점)
    ooxoo
    oxoxo
    xxxxx 으로 배열을 초기화
    """
    matrix[n][m] = '*'
    
    matrix[n+1][m-1] = '*'
    matrix[n+1][m+1] = '*'

    matrix[n+2][m-2] = '*'
    matrix[n+2][m-1] = '*'
    matrix[n+2][m] = '*'
    matrix[n+2][m+1] = '*'
    matrix[n+2][m+2] = '*'

def printStar(A):
    for row in A:
        for el in row:
            print(el)
        print("\n")

"""
input : 24
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
"""
n = int(input())
A = [[' ' for _ in range(2*n-1)] for _ in range(n)]
setStar(A,n,0,n-1)
printStar(A)