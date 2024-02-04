// clang-format off
#include <bits/stdc++.h>
using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, ll> pil;
typedef pair<ll, int> pli;
typedef pair<double, double> pdd;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
#define ALL(_a) _a.begin(), _a.end()
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define vt vector

const ll MOD = 1000000007;
const int iNF = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const ll MAXN = 100005;
const int dr[8] = {0, 0, 1, -1, 1, 1, -1, -1};
const int dc[8] = {1, -1, 0, 0, 1, -1, 1, -1};

#ifdef GP_DEBUG
#ifdef __GNUG__
#define GP_FUNC __PRETTY_FUNCTION__
#elif defined(_MSC_VER)
#define GP_FUNC __FUNCSIG__
#else
#define GP_FUNC ""
#endif  // __GNUG__
#define DEBUG(...) do { fprintf(stderr, "%s - %d (%s) = ", GP_FUNC, __LINE__, #__VA_ARGS__); _Do(__VA_ARGS__); } while(0)
#define debug(...) DEBUG(__VA_ARGS__)
template <typename T> void _Do(T &&_x) { cerr << _x << endl; }
template <typename T, typename... S> void _Do(T &&_x, S &&..._t) { cerr << _x << ", "; _Do(_t...); }
template <typename It> ostream &_DoIt(ostream &_s, It _ita, It _itb) {
  _s << "{";
  for (It _it = _ita; _it != _itb; _it++) { _s << (_it == _ita ? "" : ",") << *_it; }
  _s << "}";
  return _s;
}
template <typename T> ostream &operator<<(ostream &_s, vector<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, vector<T> &&_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, deque<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, list<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, set<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, multiset<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, unordered_set<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T> ostream &operator<<(ostream &_s, unordered_multiset<T> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T1, typename T2> ostream &operator<<(ostream &_s, map<T1, T2> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T1, typename T2> ostream &operator<<(ostream &_s, multimap<T1, T2> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T1, typename T2> ostream &operator<<(ostream &_s, unordered_map<T1, T2> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T1, typename T2> ostream &operator<<(ostream &_s, unordered_multimap<T1, T2> &_c) { return _DoIt(_s, ALL(_c)); }
template <typename T1, typename T2> ostream &operator<<(ostream &_s, pair<T1, T2> _p) { return _s << "(" << _p.first << "," << _p.second << ")"; }
class Timer {
 public:
  Timer(string name) : scope_name(name), start_time(chrono::high_resolution_clock::now()) {}
  ~Timer() {
    auto stop_time = chrono::high_resolution_clock::now();
    auto length = chrono::duration_cast<chrono::microseconds>(stop_time - start_time).count();
    double mlength = double(length) * 0.001;
    DEBUG(scope_name, mlength);
  }
 private:
  string scope_name;
  chrono::high_resolution_clock::time_point start_time;
};
#define TIME(x) Timer timer_##x(#x)
#define ASSERT(...) assert(__VA_ARGS__)
#define IOS()
#else
#define DEBUG(...)
#define debug(...)
#define TIME(...)
#define ASSERT(...) __VA_ARGS__
#define IOS() ios_base::sync_with_stdio(0); cin.tie(0)
#define endl '\n'
#endif  // GP_DEBUG
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
// clang-format on

/********** Good Luck :) **********/

#include "leetcode-helper/leetcode_util.h"
using namespace leetcode_util;

#include "@SOLUTION_SOURCE@"

int main() {
  IOS();
  TIME(main);

  Solution solution;
  // INPUT VARIABLES
  auto ans = solution.@METHOD@(@ARGUMENTS@);
  DEBUG(ans);

  return 0;
}
