#include <stdio.h>
int main()
{
  int i, j;
  int save, sum1, sum2;
  int array[4][4] = {
      {-2, 7, 6, 9},
      {13, 2, 0, 4},
      {5, 3, 3, 5},
      {1, 12, 26, -1},

  };

  for ( i = 0; i < 4; i++ ) {
    for ( j = 0; j < 4; j++ )
        {
        if (j < 3){
          sum1 += array[i][j];
          sum2 += array[i][4 - j- 1];
        }

    }
    if (sum1 == sum2)
    {
      for ( j = 0; j < 2; j++ )
        {  
            save = array[i][j];
            array[i][j] = array[i][4 - j -1];
            array[i][4 - j - 1 ] = save;
        }
    }
    else{
    }
    sum1 = 0; sum2 = 0;
  }
}
