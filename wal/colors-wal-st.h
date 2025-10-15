const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0C0E1B", /* black   */
  [1] = "#B8B659", /* red     */
  [2] = "#71A19A", /* green   */
  [3] = "#15C8E1", /* yellow  */
  [4] = "#2DE3E9", /* blue    */
  [5] = "#40DADC", /* magenta */
  [6] = "#A1B0AB", /* cyan    */
  [7] = "#dee2e1", /* white   */

  /* 8 bright colors */
  [8]  = "#9b9e9d",  /* black   */
  [9]  = "#B8B659",  /* red     */
  [10] = "#71A19A", /* green   */
  [11] = "#15C8E1", /* yellow  */
  [12] = "#2DE3E9", /* blue    */
  [13] = "#40DADC", /* magenta */
  [14] = "#A1B0AB", /* cyan    */
  [15] = "#dee2e1", /* white   */

  /* special colors */
  [256] = "#0C0E1B", /* background */
  [257] = "#dee2e1", /* foreground */
  [258] = "#dee2e1",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
