from dotenv import load_dotenv
from langchain_community.agent_toolkits import JiraToolkit
from langchain_community.utilities.jira import JiraAPIWrapper

# 加载环境变量
load_dotenv()

# 实例化 Jira 工具包
jira = JiraAPIWrapper()
jira_toolkit = JiraToolkit.from_jira_api_wrapper(jira)

# 获取工具列表
jira_tools = jira_toolkit.get_tools()

if __name__ == "__main__":
    # 打印工具的名称和描述
    print("可用的 Jira 工具如下：")
    print("=" * 30)
    for tool in jira_tools:
        print(f"工具名称: {tool.name}")
        print(f"工具描述: {tool.description}")
        print("-" * 30)
