import * as z from "zod";
import { ProjectSchema } from "./project";
import { TagSchema } from "./tag";

export const EntrySchema = z.object({
	title: z.string(),
	description: z.string().nullable(),
	start_at: z.string(),
	project: ProjectSchema,
	tags: z.array(TagSchema),
});

export type Entry = z.infer<typeof EntrySchema>;
