import { useEffect, useState } from "react";
import type { Entry } from "../../schemas/entry";

const calcElapsedTime = (now: number, startAtStr: string) => {
	const startAt = Date.parse(startAtStr);
	const elapsedSec = Math.floor((now - startAt) / 1000);

	const mm = Math.floor(elapsedSec / 60);
	const ss = String(elapsedSec % 60).padStart(2, "0");
	return `${mm}:${ss}`;
};

type Props = {
	entry: Entry;
};

export const ElapsedTime = (props: Props) => {
	const { entry } = props;
	const [now, setNow] = useState<number>(Date.now());

	useEffect(() => {
		const t = setInterval(() => setNow(Date.now()), 1000);
		return () => clearInterval(t);
	}, []);

	return (
		<div className="text-4xl xl:text-9xl font-semibold text-emerald-700">
			{calcElapsedTime(now, entry.start_at)}
		</div>
	);
};
