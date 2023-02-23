# Copyright 2023 Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import quickfix
from app.configuration import Configuration
from build_get_order import BuildGet


def main():
    """Main"""
    try:
        Configuration().build_config()
        settings = quickfix.SessionSettings('example.cfg', True)

        build = BuildGet()

        storefactory = quickfix.FileStoreFactory(settings)
        initiator = quickfix.SSLSocketInitiator(build, storefactory, settings)

        initiator.start()
        build.run_get_order()

    except (quickfix.ConfigError, quickfix.RuntimeError) as exception:
        assert type(exception).__name__ == 'NameError'


if __name__ == '__main__':
    main()
