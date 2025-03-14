This repository contains a prototype for the Extreme End-to-End FinTech LLM System, developed for the XNL LLM Task 1 challenge (March 14, 2025). It’s an AI-powered, risk-aware financial platform integrating LLMs, real-time market data, and autonomous trading. Built in 24 hours, this MVP prioritizes Phases 1 and 2, with stubs for further expansion, targeting low-latency execution, scalability, and compliance readiness.

Features
Phase 1: FinTech LLM Architecture & Data Ingestion
LLM-driven sentiment analysis (Mixtral) with <5ms target latency.
Real-time BTC/USD data via Binance WebSocket.
Multi-agent system (data aggregator, sentiment analyzer, trade decision) with Kafka.
Basic fraud detection stub.

Phase 2: AI-Powered Trading Engine
Reinforcement Learning (PPO) trading bot with historical BTC/USD backtesting.
Markowitz portfolio optimization for risk-adjusted allocation.
Tech: Python, FastAPI, Kafka, Redis, Transformers, Stable-Baselines3, yfinance.