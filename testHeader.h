 #include "cocos2d.h"

class myClass : public cocos2d::CCNode
{
 public:
  myClass();
  virtual ~myClass();

  void SetParamA(int var);
  int GetParamA();

  CC_SYNTHESIZE(int, m_paramB, ParamB);
}

