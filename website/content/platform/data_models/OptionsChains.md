---
title: Get the complete options chain for a ticker
description: OpenBB Platform Data Model
---

<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

---

## Implementation details

### Class names

| Model name | Parameters class | Data class |
| ---------- | ---------------- | ---------- |
| `OptionsChains` | `OptionsChainsQueryParams` | `OptionsChainsData` |

### Import Statement

```python
from openbb_provider.standard_models.options_chains import (
OptionsChainsData,
OptionsChainsQueryParams,
)
```

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| provider | Literal['cboe', 'intrinio'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
</TabItem>

<TabItem value='intrinio' label='intrinio'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| provider | Literal['cboe', 'intrinio'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
| date | date | Date for which the options chains are returned. |  | False |
</TabItem>

</Tabs>

## Data

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description |
| ---- | ---- | ----------- |
| contract_symbol | str | Contract symbol for the option. |
| symbol | str | Symbol representing the entity requested in the data. Here its the underlying symbol for the option. |
| expiration | date | Expiration date of the contract. |
| strike | float | Strike price of the contract. |
| option_type | str | Call or Put. |
| eod_date | date | Date for which the options chains are returned. |
| close | float | The close price. |
| close_bid | float | The closing bid price for the option that day. |
| close_ask | float | The closing ask price for the option that day. |
| volume | float | The trading volume. |
| open | float | The open price. |
| open_bid | float | The opening bid price for the option that day. |
| open_ask | float | The opening ask price for the option that day. |
| open_interest | float | Open interest on the contract. |
| high | float | The high price. |
| low | float | The low price. |
| mark | float | The mid-price between the latest bid-ask spread. |
| ask_high | float | The highest ask price for the option that day. |
| ask_low | float | The lowest ask price for the option that day. |
| bid_high | float | The highest bid price for the option that day. |
| bid_low | float | The lowest bid price for the option that day. |
| implied_volatility | float | Implied volatility of the option. |
| delta | float | Delta of the option. |
| gamma | float | Gamma of the option. |
| theta | float | Theta of the option. |
| vega | float | Vega of the option. |
</TabItem>

<TabItem value='cboe' label='cboe'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| contract_symbol | str | Contract symbol for the option. |
| symbol | str | Symbol representing the entity requested in the data. Here its the underlying symbol for the option. |
| expiration | date | Expiration date of the contract. |
| strike | float | Strike price of the contract. |
| option_type | str | Call or Put. |
| eod_date | date | Date for which the options chains are returned. |
| close | float | The close price. |
| close_bid | float | The closing bid price for the option that day. |
| close_ask | float | The closing ask price for the option that day. |
| volume | float | The trading volume. |
| open | float | The open price. |
| open_bid | float | The opening bid price for the option that day. |
| open_ask | float | The opening ask price for the option that day. |
| open_interest | float | Open interest on the contract. |
| high | float | The high price. |
| low | float | The low price. |
| mark | float | The mid-price between the latest bid-ask spread. |
| ask_high | float | The highest ask price for the option that day. |
| ask_low | float | The lowest ask price for the option that day. |
| bid_high | float | The highest bid price for the option that day. |
| bid_low | float | The lowest bid price for the option that day. |
| implied_volatility | float | Implied volatility of the option. |
| delta | float | Delta of the option. |
| gamma | float | Gamma of the option. |
| theta | float | Theta of the option. |
| vega | float | Vega of the option. |
| bid_size | int | Bid size for the option. |
| ask_size | int | Ask size for the option. |
| theoretical | float | Theoretical value of the option. |
| last_trade_price | float | Last trade price of the option. |
| tick | str | Whether the last tick was up or down in price. |
| prev_close | float | Previous closing price of the option. |
| change | float | Change in  price of the option. |
| change_percent | float | Change, in percent, of the option. |
| rho | float | Rho of the option. |
| last_trade_timestamp | datetime | Last trade timestamp of the option. |
| dte | int | Days to expiration for the option. |
</TabItem>

</Tabs>

