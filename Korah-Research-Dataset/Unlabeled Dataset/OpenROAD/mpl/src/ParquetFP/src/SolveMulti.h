/**************************************************************************
***
*** Copyright (c) 2000-2006 Regents of the University of Michigan,
***               Saurabh N. Adya, Hayward Chan, Jarrod A. Roy
***               and Igor L. Markov
***
***  Contact author(s): sadya@umich.edu, imarkov@umich.edu
***  Original Affiliation:   University of Michigan, EECS Dept.
***                          Ann Arbor, MI 48109-2122 USA
***
***  Permission is hereby granted, free of charge, to any person obtaining
***  a copy of this software and associated documentation files (the
***  "Software"), to deal in the Software without restriction, including
***  without limitation
***  the rights to use, copy, modify, merge, publish, distribute, sublicense,
***  and/or sell copies of the Software, and to permit persons to whom the
***  Software is furnished to do so, subject to the following conditions:
***
***  The above copyright notice and this permission notice shall be included
***  in all copies or substantial portions of the Software.
***
*** THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
*** EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
*** OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
*** IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
*** CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
*** OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
*** THE USE OR OTHER DEALINGS IN THE SOFTWARE.
***
***
***************************************************************************/

#ifndef SOLVEMULTI_H
#define SOLVEMULTI_H

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>

namespace parquetfp {
class DB;
class Command_Line;

class SolveMulti
{
 private:
  DB* _db;
  Command_Line* _params;
  DB* _newDB;

 public:
  SolveMulti(DB* db, Command_Line* params);
  ~SolveMulti();
  void go();
  DB* clusterOnly() const;

  void placeSubBlocks();
  void updatePlaceUnCluster(DB* clusterDB);

  mutable float clusterTime;
  mutable float annealTime;
};
}  // namespace parquetfp
// using namespace parquetfp;

#endif
