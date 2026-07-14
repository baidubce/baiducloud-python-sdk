2026-07-14 Version: 0.0.2
新增OAuth2客户端、IdP配置及Agent身份管理接口响应字段
- 涉及产品: AGENTIDENTITY，createOauth2Client/updateOauth2Client/getOauth2Client新增clientId、clientSecret等字段
- 涉及产品: AGENTIDENTITY，createIdpConfiguration/updateIdpConfiguration/getIdpConfiguration/disableIdpConfiguration/enableIdpConfiguration新增idpType、discoveryUrl等字段
- 涉及产品: AGENTIDENTITY，createAgent/getAgent/updateAgent新增bceDomainId、extra等字段，凭证提供方接口新增完整OIDC配置字段
- 涉及产品: AGENTIDENTITY，createUserPool/getUserPool/createUser/getUser/updateUser新增统计、端点及来源字段

2026-07-07 Version: 0.0.1
- 涉及产品: AGENTIDENTITY，新增Agent创建、查询、更新、删除接口
- 涉及产品: AGENTIDENTITY，新增用户池及用户的增删改查与批量获取接口
- 涉及产品: AGENTIDENTITY，新增IdP配置创建、更新、启用、禁用及OAuth2回调接口
- 涉及产品: AGENTIDENTITY，新增OAuth2客户端、凭证提供方及Token获取接口
