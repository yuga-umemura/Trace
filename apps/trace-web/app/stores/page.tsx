type Store = {
  id: string;
  name: string;
  area: string;
};

export default async function StoresPage() {
  const res = await fetch(`${process.env.API_BASE_URL}/stores`, {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch stores");
  }

  const stores: Store[] = await res.json();

  return (
    <main>
      <h1>店舗一覧</h1>

      <ul>
        {stores.map((store) => (
          <li key={store.id}>
            {store.name} / {store.area}
          </li>
        ))}
      </ul>
    </main>
  );
}
