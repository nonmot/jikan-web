import * as z from "zod";

export const ProjectSchema = z.object({
	name: z.string(),
	description: z.string().nullable(),
	archived: z.boolean(),
});

export type Project = z.infer<typeof ProjectSchema>;
