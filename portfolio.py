assets = {"BTC-USD": "crypto", "AAPL": "stock"}
data = yf.download(list(assets.keys())[0], start="2024-01-01", end="2025-03-13")

# Install: pip install cvxpy
import cvxpy as cp

returns = data["Close"].pct_change().dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()

weights = cp.Variable(len(mean_returns))
portfolio_return = mean_returns @ weights
portfolio_risk = cp.quad_form(weights, cov_matrix)

objective = cp.Maximize(portfolio_return - 0.5 * portfolio_risk)  # Risk-adjusted return
constraints = [cp.sum(weights) == 1, weights >= 0]
problem = cp.Problem(objective, constraints)
problem.solve()

print(f"Optimal Weights: {weights.value}")