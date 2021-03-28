# python
The Time in Words

Given the time in numerals we may convert it into words, as shown below:
                                                  5:00 → five o’clock
                                                  5:01 → one minute past five
                                                  5:10 → ten minutes past five
                                                  5:15 → quarter past five
                                                  5:28 → twenty eight minutes past five 5:30 → half past five
                                                  5:40 → twenty minutes past six
                                                  5:45 → quarter past six
                                                  5:47 → thirteen minutes to six
At minutes = 0, use o’clock. For 1 < minutes < 30, use past, and for 30 < minutes use to.

Function Description:
In your function, you are required to have the following parameters(s): int h – the hour of the day and int m – the minutes after the hour. Which will return a string, a time string as it has been mentioned. The input format should be, the first line contains h, the hours portion and the second line contain m, the minutes portion. Therefore, the constraints should be the following (Hackerrank, n.d.):
                                                 • 1<h<12 • 0<m<60

Sample          Input         Output
                  5
 1                47          thirteen minutes to six
 
                  7
 2                15          quarter past seven
