import { useQuery } from "@tanstack/react-query";
import { EntrySchema } from "../../schemas/entry";
import type { Tag } from "../../schemas/tag";
import { ElapsedTime } from "../ElapsedTime";

const getRunningEntry = async () => {
	const res = await fetch(
		`${import.meta.env.VITE_API_BASE_URL}/entries/running`,
	);

	if (!res.ok) {
		const text = await res.text().catch(() => "");
		throw new Error(`HTTP ${res.status} ${res.statusText} ${text}`);
	}

	if (res.status === 204) return null;

	const data = await res.json();
	return EntrySchema.parse(data);
};

const useRunningEntryPolling = () => {
	const { data, isLoading } = useQuery({
		queryKey: ["Entry"],
		queryFn: async () => {
			const entry = await getRunningEntry();
			return entry;
		},
		refetchInterval: 10000,
	});
	return {
		entry: data,
		isLoading,
	};
};

const parseDatetime = (dateStr: string) => {
	return new Date(dateStr).toLocaleString();
};

export const EntryCard = () => {
	const { entry, isLoading } = useRunningEntryPolling();

	if (isLoading) {
		return <div>Loading</div>;
	}

	if (!entry) {
		return (
			<div>
				<div className="rounded-xl border bg-white p-4 shadow-sm">
					<div>No running entry</div>
				</div>
			</div>
		);
	}

	return (
		<div className="rounded-xl border bg-white p-4 shadow-sm">
			{entry.project ? (
				<div className="text-sm text-slate-500">{entry.project.name}</div>
			) : null}

			<div className="mt-1 text-base font-semibold text-slate-900">
				{entry.title ? entry.title : "No title"}
			</div>

			<div className="mt-2 text-sm text-slate-600">
				{entry.description ? entry.description : ""}
			</div>

			<div className="mt-3 grid grid-cols-2 gap-3 text-sm">
				<div>
					<div className="text-xs text-slate-500">Started</div>
					<div className="text-slate-900">{parseDatetime(entry.start_at)}</div>
				</div>
				<div>
					<div className="text-xs text-slate-500">Elapsed</div>
					<ElapsedTime entry={entry} />
				</div>
			</div>

			{entry.tags && entry.tags.length > 0 ? (
				<div className="mt-3 flex flex-wrap gap-2">
					{entry.tags.map((tag: Tag) => (
						<span
							key={tag.name}
							className="rounded-full border px-2 py-0.5 text-xs text-slate-700"
						>
							{tag.name}
						</span>
					))}
				</div>
			) : null}
		</div>
	);
};
