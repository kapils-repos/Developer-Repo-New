---
id: "Cl0001"
artifactTitle: SubjectScheme Map
talendVersion: 7.1.1
artifactTags: Documentation, DITA, Taxonomy
author: "Travis CI"
artifactVersion: "1"
---

# SubjectScheme map 

Subject scheme maps use key definitions to define collections of controlled values and subject definitions.

Controlled values are keywords that can be used as values for attributes.For example, the @audience attribute can take a value that identifies the users that are associated with a particular product. Typical values for a medical-equipment product line might include "therapist", "oncologist", "physicist", and "radiologist". In a subject scheme map, an information architect can define a list of these values for the @audience attribute. Controlled values can be used to classify content for filtering and flagging at build time.

Subject definitions are classifications and sub-classifications that compose a tree. Subject definitions provide semantics that can be used in conjunction with taxonomies and ontologies. In conjunction with the classification domain, subject definitions can be used for retrieval and traversal of the content at run time when used with information viewing applications that provide such functionality.

Key references to controlled values are resolved to a key definition using the same precedence rules as apply to any other key. However, once a key is resolved to a controlled value, that key reference does not typically result in links or generated text.
