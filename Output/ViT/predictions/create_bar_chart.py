import matplotlib.pyplot as plt
import os
import numpy as np

# 设置数据值
dist = 0.3490
prob = 0.819002 # 98.2811% 转换为小数形式

# 创建图表
fig, ax1 = plt.subplots(figsize=(8, 5))

# 设置柱状图参数，使柱子更近
width = 0.3
bar_positions = [0.3, 0.7]  # 柱状图位置更近

# 绘制距离柱状图
ax1.bar(bar_positions[0], dist, width, color='blue', label='Distance')
ax1.set_ylabel('Distance', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 设置左侧y轴的上限，使柱子看起来更矮
y_limit = 2  # 固定值
ax1.set_ylim(0, y_limit)

ax1.set_xticks(bar_positions)
ax1.set_xticklabels(['Distance', 'Probability'])

# 在Distance柱状图上添加数值标签
ax1.text(bar_positions[0], dist + y_limit * 0.02, f"{dist:.4f}", ha='center', va='bottom', color='blue')

# 创建右侧坐标轴（准确率 %）
ax2 = ax1.twinx()
ax2.bar(bar_positions[1], prob*100, width, color='orange', label='Probability')
ax2.set_ylabel('Similarity (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(0, 110)  # 设置y轴范围，留出空间显示标签

# 在Probability柱状图上添加数值标签
ax2.text(bar_positions[1], prob*100 + 3, f"{prob*100:.4f}%", ha='center', va='bottom', color='orange')

# 添加标题和调整布局
plt.title('ViT Model Prediction of Thatcher Illusion2')
plt.tight_layout()

# 保存图片
save_path = "ViT_prediction_Thatcher2.png"
plt.savefig(save_path, dpi=300)
print(f"已保存图表 → {save_path}")

# 显示图表
plt.close()  # 关闭图表而不显示（在服务器环境中）
print("图表已生成完成！数据值已更新：dist=0.0954, prob=98.2811%") 