import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_4.complete_the_photo_pattern import pattern


ans1 = '''\
   + +   
  +o o+  
 +  u  + 
  + ~ +  
    |    
  +-o-+  
_/| o |\\_
  +-o-+  
   I I   '''

ans4 = '''\
             + +              
   + +      +o o+             
  +o o+    +  u  +      + +   
 +  u  +    + ~ +      +o o+  
  + ~ +       |       +  u  + 
    |       +-o-+      + ~ +  
  +-o-+    /| o |\       |    
_/| o |\__/ +-o-+ \    +-o-+  
  +-o-+      | |   \__/| o |\_
   | |       | |       +-o-+  
   I I       I I        I I   '''

ans5 = '''\
                       + +                       
             + +      +o o+                      
   + +      +o o+    +  u  +      + +      + +   
  +o o+    +  u  +    + ~ +      +o o+    +o o+  
 +  u  +    + ~ +       |       +  u  +  +  u  + 
  + ~ +       |       +-o-+      + ~ +    + ~ +  
    |       +-o-+    /| o |\       |        |    
  +-o-+    /| o |\__/ +-o-+ \    +-o-+    +-o-+  
_/| o |\__/ +-o-+      | |   \__/| o |\__/| o |\_
  +-o-+      | |       | |       +-o-+    +-o-+  
   I I       I I       I I        I I      I I   '''

test.assert_equals(pattern([1]),  ans1)
test.assert_equals(pattern([2]), '   + +   \n  +o o+  \n +  u  + \n  + ~ +  \n    |    \n  +-o-+  \n_/| o |\\_\n  +-o-+  \n   | |   \n   I I   ')
test.assert_equals(pattern([3]), '   + +   \n  +o o+  \n +  u  + \n  + ~ +  \n    |    \n  +-o-+  \n_/| o |\\_\n  +-o-+  \n   | |   \n   | |   \n   I I   ')
test.assert_equals(pattern([1,2,3]), ans4)
test.assert_equals(pattern([2,3,1,1,1]), ans5)