# 一生一芯一键testbench并生成波形文件
## 使用
> 请确保你的测试文件名为`testbench.cpp`

在你的`testbench.cpp`中，你可能需要像下面这样
```cpp
#include "Vsim_module.h"

int main(int argc, char **argv) {
    VerilatedContext* contextp = new VerilatedContext;
    contextp->commandArgs(argc, argv);
    Vsim_module* sim_module = new Vsim_module{contextp};
    ...
}
```

```bash
# 运行
bash onekey run file1.v file2.v ...
# 清除
bash onekey clean
```