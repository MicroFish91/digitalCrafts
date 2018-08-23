-- SELECT * FROM project
--   JOIN project_uses_tech ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = 3;

-- SELECT * FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = 4
--   JOIN tech ON project_uses_tech.tech_id = tech.id;

-- SELECT tech.id FROM tech
--   LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id where project_uses_tech.project_id IS NULL;

-- SELECT project.name, count(tech.id) FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = tech.id
--   GROUP BY project.name;

-- SELECT project.name FROM project
--   LEFT OUTER JOIN project_uses_tech ON project_uses_tech.project_id = project.id where project_uses_tech.tech_id IS NULL;

-- SELECT tech.name, count(project.id) FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = tech.id
--   GROUP BY tech.name

-- SELECT * FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = tech.id

-- SELECT distinct (tech.name) FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = tech.id

-- SELECT distinct (tech.name) FROM tech
--     LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id where project_uses_tech.project_id IS NULL

-- SELECT distinct (project.name) FROM project_uses_tech
--   JOIN project ON project_uses_tech.project_id = project.id
--   JOIN tech ON project_uses_tech.tech_id = tech.id

-- SELECT distinct (project.name) FROM project
--     LEFT OUTER JOIN project_uses_tech ON project_uses_tech.project_id = project.id where project_uses_tech.tech_id IS NULL

-- SELECT project.name, count(tech.name) FROM project_uses_tech
--     FULL OUTER JOIN project ON project_uses_tech.project_id = project.id
--     FULL OUTER JOIN tech ON  project_uses_tech.tech_id = tech.id
--     GROUP BY project.name
--     ORDER BY count DESC

SELECT avg(count) from (SELECT tech.id, tech.name, count(tech.id) FROM project_uses_tech
        JOIN project ON project_uses_tech.project_id = project.id
        JOIN tech ON project_uses_tech.tech_id = tech.id
        GROUP BY tech.id) as ffuck_you