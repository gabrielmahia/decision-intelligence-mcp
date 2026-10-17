FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/decision-intelligence-mcp"
LABEL org.opencontainers.image.description="decision-intelligence-mcp: MCP server over stdio, no credentials needed"
LABEL org.opencontainers.image.licenses="MIT"
# Installs the latest published release from PyPI (do not pin: a pinned version made Glama inspect an old release of mpesa-mcp).
RUN pip install --no-cache-dir decision-intelligence-mcp
CMD ["decision-intelligence-mcp"]
