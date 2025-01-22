"""
This type stub file was generated by pyright.
"""

class ImplicitAPI:
    publicWalletGetCurrencyChains = ...
    publicSpotGetCurrencies = ...
    publicSpotGetCurrenciesCurrency = ...
    publicSpotGetCurrencyPairs = ...
    publicSpotGetCurrencyPairsCurrencyPair = ...
    publicSpotGetTickers = ...
    publicSpotGetOrderBook = ...
    publicSpotGetTrades = ...
    publicSpotGetCandlesticks = ...
    publicSpotGetTime = ...
    publicMarginGetCurrencyPairs = ...
    publicMarginGetCurrencyPairsCurrencyPair = ...
    publicMarginGetFundingBook = ...
    publicMarginGetCrossCurrencies = ...
    publicMarginGetCrossCurrenciesCurrency = ...
    publicMarginGetUniCurrencyPairs = ...
    publicMarginGetUniCurrencyPairsCurrencyPair = ...
    publicFlash_swapGetCurrencies = ...
    publicFuturesGetSettleContracts = ...
    publicFuturesGetSettleContractsContract = ...
    publicFuturesGetSettleOrderBook = ...
    publicFuturesGetSettleTrades = ...
    publicFuturesGetSettleCandlesticks = ...
    publicFuturesGetSettlePremiumIndex = ...
    publicFuturesGetSettleTickers = ...
    publicFuturesGetSettleFundingRate = ...
    publicFuturesGetSettleInsurance = ...
    publicFuturesGetSettleContractStats = ...
    publicFuturesGetSettleIndexConstituentsIndex = ...
    publicFuturesGetSettleLiqOrders = ...
    publicFuturesGetSettleRiskLimitTiers = ...
    publicDeliveryGetSettleContracts = ...
    publicDeliveryGetSettleContractsContract = ...
    publicDeliveryGetSettleOrderBook = ...
    publicDeliveryGetSettleTrades = ...
    publicDeliveryGetSettleCandlesticks = ...
    publicDeliveryGetSettleTickers = ...
    publicDeliveryGetSettleInsurance = ...
    publicOptionsGetUnderlyings = ...
    publicOptionsGetExpirations = ...
    publicOptionsGetContracts = ...
    publicOptionsGetContractsContract = ...
    publicOptionsGetSettlements = ...
    publicOptionsGetSettlementsContract = ...
    publicOptionsGetOrderBook = ...
    publicOptionsGetTickers = ...
    publicOptionsGetUnderlyingTickersUnderlying = ...
    publicOptionsGetCandlesticks = ...
    publicOptionsGetUnderlyingCandlesticks = ...
    publicOptionsGetTrades = ...
    publicEarnGetUniCurrencies = ...
    publicEarnGetUniCurrenciesCurrency = ...
    privateWithdrawalsPostWithdrawals = ...
    privateWithdrawalsPostPush = ...
    privateWithdrawalsDeleteWithdrawalsWithdrawalId = ...
    privateWalletGetDepositAddress = ...
    privateWalletGetWithdrawals = ...
    privateWalletGetDeposits = ...
    privateWalletGetSubAccountTransfers = ...
    privateWalletGetOrderStatus = ...
    privateWalletGetWithdrawStatus = ...
    privateWalletGetSubAccountBalances = ...
    privateWalletGetSubAccountMarginBalances = ...
    privateWalletGetSubAccountFuturesBalances = ...
    privateWalletGetSubAccountCrossMarginBalances = ...
    privateWalletGetSavedAddress = ...
    privateWalletGetFee = ...
    privateWalletGetTotalBalance = ...
    privateWalletGetSmallBalance = ...
    privateWalletGetSmallBalanceHistory = ...
    privateWalletGetPush = ...
    privateWalletPostTransfers = ...
    privateWalletPostSubAccountTransfers = ...
    privateWalletPostSubAccountToSubAccount = ...
    privateWalletPostSmallBalance = ...
    privateSubAccountsGetSubAccounts = ...
    privateSubAccountsGetSubAccountsUserId = ...
    privateSubAccountsGetSubAccountsUserIdKeys = ...
    privateSubAccountsGetSubAccountsUserIdKeysKey = ...
    privateSubAccountsPostSubAccounts = ...
    privateSubAccountsPostSubAccountsUserIdKeys = ...
    privateSubAccountsPostSubAccountsUserIdLock = ...
    privateSubAccountsPostSubAccountsUserIdUnlock = ...
    privateSubAccountsPutSubAccountsUserIdKeysKey = ...
    privateSubAccountsDeleteSubAccountsUserIdKeysKey = ...
    privateUnifiedGetAccounts = ...
    privateUnifiedGetAccountMode = ...
    privateUnifiedGetBorrowable = ...
    privateUnifiedGetTransferable = ...
    privateUnifiedGetLoans = ...
    privateUnifiedGetLoanRecords = ...
    privateUnifiedGetInterestRecords = ...
    privateUnifiedGetEstimateRate = ...
    privateUnifiedGetCurrencyDiscountTiers = ...
    privateUnifiedGetRiskUnits = ...
    privateUnifiedGetUnifiedMode = ...
    privateUnifiedGetLoanMarginTiers = ...
    privateUnifiedGetLeverageUserCurrencyConfig = ...
    privateUnifiedGetLeverageUserCurrencySetting = ...
    privateUnifiedPostAccountMode = ...
    privateUnifiedPostLoans = ...
    privateUnifiedPostPortfolioCalculator = ...
    privateUnifiedPostLeverageUserCurrencySetting = ...
    privateUnifiedPutUnifiedMode = ...
    privateSpotGetFee = ...
    privateSpotGetBatchFee = ...
    privateSpotGetAccounts = ...
    privateSpotGetAccountBook = ...
    privateSpotGetOpenOrders = ...
    privateSpotGetOrders = ...
    privateSpotGetOrdersOrderId = ...
    privateSpotGetMyTrades = ...
    privateSpotGetPriceOrders = ...
    privateSpotGetPriceOrdersOrderId = ...
    privateSpotPostBatchOrders = ...
    privateSpotPostCrossLiquidateOrders = ...
    privateSpotPostOrders = ...
    privateSpotPostCancelBatchOrders = ...
    privateSpotPostCountdownCancelAll = ...
    privateSpotPostAmendBatchOrders = ...
    privateSpotPostPriceOrders = ...
    privateSpotDeleteOrders = ...
    privateSpotDeleteOrdersOrderId = ...
    privateSpotDeletePriceOrders = ...
    privateSpotDeletePriceOrdersOrderId = ...
    privateSpotPatchOrdersOrderId = ...
    privateMarginGetAccounts = ...
    privateMarginGetAccountBook = ...
    privateMarginGetFundingAccounts = ...
    privateMarginGetAutoRepay = ...
    privateMarginGetTransferable = ...
    privateMarginGetLoans = ...
    privateMarginGetLoansLoanId = ...
    privateMarginGetLoansLoanIdRepayment = ...
    privateMarginGetLoanRecords = ...
    privateMarginGetLoanRecordsLoanRecordId = ...
    privateMarginGetBorrowable = ...
    privateMarginGetCrossAccounts = ...
    privateMarginGetCrossAccountBook = ...
    privateMarginGetCrossLoans = ...
    privateMarginGetCrossLoansLoanId = ...
    privateMarginGetCrossRepayments = ...
    privateMarginGetCrossInterestRecords = ...
    privateMarginGetCrossTransferable = ...
    privateMarginGetCrossEstimateRate = ...
    privateMarginGetCrossBorrowable = ...
    privateMarginGetUniEstimateRate = ...
    privateMarginGetUniLoans = ...
    privateMarginGetUniLoanRecords = ...
    privateMarginGetUniInterestRecords = ...
    privateMarginGetUniBorrowable = ...
    privateMarginPostAutoRepay = ...
    privateMarginPostLoans = ...
    privateMarginPostMergedLoans = ...
    privateMarginPostLoansLoanIdRepayment = ...
    privateMarginPostCrossLoans = ...
    privateMarginPostCrossRepayments = ...
    privateMarginPostUniLoans = ...
    privateMarginPatchLoansLoanId = ...
    privateMarginPatchLoanRecordsLoanRecordId = ...
    privateMarginDeleteLoansLoanId = ...
    privateFlash_swapGetCurrencies = ...
    privateFlash_swapGetCurrencyPairs = ...
    privateFlash_swapGetOrders = ...
    privateFlash_swapGetOrdersOrderId = ...
    privateFlash_swapPostOrders = ...
    privateFlash_swapPostOrdersPreview = ...
    privateFuturesGetSettleAccounts = ...
    privateFuturesGetSettleAccountBook = ...
    privateFuturesGetSettlePositions = ...
    privateFuturesGetSettlePositionsContract = ...
    privateFuturesGetSettleDualCompPositionsContract = ...
    privateFuturesGetSettleOrders = ...
    privateFuturesGetSettleOrdersTimerange = ...
    privateFuturesGetSettleOrdersOrderId = ...
    privateFuturesGetSettleMyTrades = ...
    privateFuturesGetSettleMyTradesTimerange = ...
    privateFuturesGetSettlePositionClose = ...
    privateFuturesGetSettleLiquidates = ...
    privateFuturesGetSettleAutoDeleverages = ...
    privateFuturesGetSettleFee = ...
    privateFuturesGetSettleRiskLimitTiers = ...
    privateFuturesGetSettlePriceOrders = ...
    privateFuturesGetSettlePriceOrdersOrderId = ...
    privateFuturesPostSettlePositionsContractMargin = ...
    privateFuturesPostSettlePositionsContractLeverage = ...
    privateFuturesPostSettlePositionsContractRiskLimit = ...
    privateFuturesPostSettleDualMode = ...
    privateFuturesPostSettleDualCompPositionsContractMargin = ...
    privateFuturesPostSettleDualCompPositionsContractLeverage = ...
    privateFuturesPostSettleDualCompPositionsContractRiskLimit = ...
    privateFuturesPostSettleOrders = ...
    privateFuturesPostSettleBatchOrders = ...
    privateFuturesPostSettleCountdownCancelAll = ...
    privateFuturesPostSettleBatchCancelOrders = ...
    privateFuturesPostSettlePriceOrders = ...
    privateFuturesPutSettleOrdersOrderId = ...
    privateFuturesDeleteSettleOrders = ...
    privateFuturesDeleteSettleOrdersOrderId = ...
    privateFuturesDeleteSettlePriceOrders = ...
    privateFuturesDeleteSettlePriceOrdersOrderId = ...
    privateDeliveryGetSettleAccounts = ...
    privateDeliveryGetSettleAccountBook = ...
    privateDeliveryGetSettlePositions = ...
    privateDeliveryGetSettlePositionsContract = ...
    privateDeliveryGetSettleOrders = ...
    privateDeliveryGetSettleOrdersOrderId = ...
    privateDeliveryGetSettleMyTrades = ...
    privateDeliveryGetSettlePositionClose = ...
    privateDeliveryGetSettleLiquidates = ...
    privateDeliveryGetSettleSettlements = ...
    privateDeliveryGetSettlePriceOrders = ...
    privateDeliveryGetSettlePriceOrdersOrderId = ...
    privateDeliveryPostSettlePositionsContractMargin = ...
    privateDeliveryPostSettlePositionsContractLeverage = ...
    privateDeliveryPostSettlePositionsContractRiskLimit = ...
    privateDeliveryPostSettleOrders = ...
    privateDeliveryPostSettlePriceOrders = ...
    privateDeliveryDeleteSettleOrders = ...
    privateDeliveryDeleteSettleOrdersOrderId = ...
    privateDeliveryDeleteSettlePriceOrders = ...
    privateDeliveryDeleteSettlePriceOrdersOrderId = ...
    privateOptionsGetMySettlements = ...
    privateOptionsGetAccounts = ...
    privateOptionsGetAccountBook = ...
    privateOptionsGetPositions = ...
    privateOptionsGetPositionsContract = ...
    privateOptionsGetPositionClose = ...
    privateOptionsGetOrders = ...
    privateOptionsGetOrdersOrderId = ...
    privateOptionsGetMyTrades = ...
    privateOptionsGetMmp = ...
    privateOptionsPostOrders = ...
    privateOptionsPostCountdownCancelAll = ...
    privateOptionsPostMmp = ...
    privateOptionsPostMmpReset = ...
    privateOptionsDeleteOrders = ...
    privateOptionsDeleteOrdersOrderId = ...
    privateEarnGetUniCurrencies = ...
    privateEarnGetUniCurrenciesCurrency = ...
    privateEarnGetUniLends = ...
    privateEarnGetUniLendRecords = ...
    privateEarnGetUniInterestsCurrency = ...
    privateEarnGetUniInterestRecords = ...
    privateEarnGetUniInterestStatusCurrency = ...
    privateEarnPostUniLends = ...
    privateEarnPutUniInterestReinvest = ...
    privateEarnPatchUniLends = ...
    privateLoanGetCollateralOrders = ...
    privateLoanGetCollateralOrdersOrderId = ...
    privateLoanGetCollateralRepayRecords = ...
    privateLoanGetCollateralCollaterals = ...
    privateLoanGetCollateralTotalAmount = ...
    privateLoanGetCollateralLtv = ...
    privateLoanGetCollateralCurrencies = ...
    privateLoanGetMultiCollateralOrders = ...
    privateLoanGetMultiCollateralOrdersOrderId = ...
    privateLoanGetMultiCollateralRepay = ...
    privateLoanGetMultiCollateralMortgage = ...
    privateLoanGetMultiCollateralCurrencyQuota = ...
    privateLoanGetMultiCollateralCurrencies = ...
    privateLoanGetMultiCollateralLtv = ...
    privateLoanGetMultiCollateralFixedRate = ...
    privateLoanGetMultiCollateralCurrentRate = ...
    privateLoanPostCollateralOrders = ...
    privateLoanPostCollateralRepay = ...
    privateLoanPostCollateralCollaterals = ...
    privateLoanPostMultiCollateralOrders = ...
    privateLoanPostMultiCollateralRepay = ...
    privateLoanPostMultiCollateralMortgage = ...
    privateAccountGetDetail = ...
    privateAccountGetRateLimit = ...
    privateAccountGetStpGroups = ...
    privateAccountGetStpGroupsStpIdUsers = ...
    privateAccountGetStpGroupsDebitFee = ...
    privateAccountPostStpGroups = ...
    privateAccountPostStpGroupsStpIdUsers = ...
    privateAccountDeleteStpGroupsStpIdUsers = ...
    privateRebateGetAgencyTransactionHistory = ...
    privateRebateGetAgencyCommissionHistory = ...


