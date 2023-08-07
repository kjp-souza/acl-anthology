# Copyright 2023 Marcel Bollmann <marcel@bollmann.me>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .people import Name, NameSpecification


class AmbiguousNameError(Exception):
    """Raised when an ambiguous name would need an explicit and unique ID, but does not have one.

    Attributes:
        name (Name): The name that raised the error.
    """

    def __init__(self, name: Name, message: str) -> None:
        super().__init__(message)
        self.name = name
        self.add_note("Did you forget to add an explicit/unique ID to this name?")


class NameIDUndefinedError(Exception):
    """Raised when an `<author>` or `<editor>` was used with an ID which was not defined in `name_variants.yaml`.

    Attributes:
        name_spec (NameSpecification): The name specification that raised the error.
    """

    def __init__(self, name_spec: NameSpecification) -> None:
        super().__init__(
            f"Name '{name_spec.name}' used with ID '{name_spec.id}' that doesn't exist"
        )
        self.name_spec = name_spec
        self.add_note("Did you forget to define the ID in name_variants.yaml?")
