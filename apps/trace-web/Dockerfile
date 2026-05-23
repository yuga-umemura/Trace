FROM public.ecr.aws/docker/library/node:24.15-alpine AS base
RUN npm install -g corepack
RUN corepack enable

FROM base AS builder
WORKDIR /app

COPY . .
RUN pnpm dlx turbo@^2 prune trace-web --docker
RUN rm -f ./out/full/apps/trace-web/.env.local

FROM base AS installer
WORKDIR /app

COPY --from=builder /app/out/json .
RUN pnpm install --frozen-lockfile

COPY --from=builder /app/out/full .
RUN pnpm build --filter trace-web

FROM public.ecr.aws/docker/library/node:24.15-alpine AS runner
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=installer --chown=nextjs:nodejs /app/apps/trace-web/.next/standalone ./
COPY --from=installer --chown=nextjs:nodejs /app/apps/trace-web/.next/static ./apps/trace-web/.next/static
COPY --from=installer --chown=nextjs:nodejs /app/apps/trace-web/public ./apps/trace-web/public

EXPOSE 3000

CMD ["node", "apps/trace-web/server.js"]