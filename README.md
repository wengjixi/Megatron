								megatron系统
								version:1.3
							语言:python+django+JQ+ansible编写而成，
				主要功能包括： 1，发布的代码按照项目进行划分，包括了项目的添加删除和修改，项目下包括要上传的主机及其主机的添加删除和修改 
	       				       2，代码发布采用ansible管理工具进行发布，根据ansible1.9的api来获取返回结果，并进行处理 
	       				       3，代码发布包括批量和单个文件的发布及其校验，批量采用的是版本号的校验形式，单个则是使用MD5值进行校验，保证代码上传的准确性 
	       				       4，日志审计可记录每次的代码上传情况
	       				       5，支持权限划分