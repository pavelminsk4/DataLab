<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Expert filter</span>
    </template>

    <SaveAsModal
      v-if="isOpenSaveAsModal"
      :expert-query="expertQuery"
      @close="isOpenSaveAsModal = false"
    />

    <div class="wrapper">
      <section class="expert-filter-section">
        <ExpertField
          v-if="isShowExpertInput"
          v-model="expertQuery"
          label="Filter query"
        />

        <div class="expert-filter-buttons">
          <BaseButton v-if="false" :is-not-background="true"
            >Detailed search syntax</BaseButton
          >
          <BaseButton :is-not-background="true" @click="resetQuery"
            ><PlusIcon class="reset-icon" />Reset</BaseButton
          >
        </div>
      </section>

      <section class="presets-section">
        <div class="preset-label">Presets</div>
        <div>
          <BaseInput v-model="searchPreset" />

          <ul class="preset-groups scroll">
            <template
              v-for="{id: groupId, title, presets} in groups"
              :key="groupId"
            >
              <li
                class="group"
                @click="isClosedGroup[title] = !isClosedGroup[title]"
              >
                <BaseCheckbox
                  :checked="presets.length === selectedPresets[groupId]?.length"
                  @update:modelValue="isGroupChecked($event, groupId, presets)"
                />
                <span>{{ title }}</span>

                <ArrowheadIcon
                  :direction="isClosedGroup[title] ? 'top' : 'down'"
                />
              </li>
              <template v-if="!isClosedGroup[title]">
                <li
                  v-for="(preset, index) in presets"
                  :key="preset.id"
                  :class="[
                    'preset',
                    index + 1 === presets.length && 'mb',
                    activePreset === preset.id && 'active-preset',
                  ]"
                >
                  <BaseCheckbox
                    v-model="selectedPresets[groupId]"
                    :id="preset.id"
                  />
                  <span>{{ preset.title }}</span>
                  <button
                    v-if="activePreset !== preset.id"
                    class="edit-preset-btn"
                    @click="editPreset(preset)"
                  >
                    <EditIcon />
                  </button>
                </li>
              </template>
            </template>
          </ul>
        </div>
      </section>
    </div>

    <footer class="footer">
      <BaseButton :is-not-background="true" @click="openSaveAsModal"
        >Save as</BaseButton
      >
      <BaseButton :is-not-background="true" @click="updatePreset"
        >Save</BaseButton
      >
      <BaseButton @click="addFilterToProject">Add Filter</BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import {nextTick} from 'vue'
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import PlusIcon from '@components/icons/PlusIcon'
import BaseButton from '@components/common/BaseButton'
import BaseModal from '@components/modals/BaseModal'
import ExpertField from '@components/expert-filter/ExpertField'
import BaseInput from '@components/common/BaseInput'
import BaseCheckbox from '@components/BaseCheckbox'
import ArrowheadIcon from '@components/icons/ArrowheadIcon'
import EditIcon from '@components/icons/EditIcon'

import SaveAsModal from '@components/expert-filter/SaveAsModal'

const {mapActions, mapGetters} = createNamespacedHelpers('expertFilter')

export default {
  name: 'ExpertFilterModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
    ExpertField,
    BaseCheckbox,
    ArrowheadIcon,
    EditIcon,
    SaveAsModal,
    PlusIcon,
  },
  emits: ['add-expert-filter'],
  props: {
    projectPresets: {type: Array, default: () => []},
  },
  data() {
    return {
      expertQuery: [''],
      isShowExpertInput: true,
      searchPreset: '',
      isClosedGroup: {},
      isOpenSaveAsModal: false,
      isOpenCreateGroupModal: false,
      editablePreset: null,
      activePreset: 0,
      selectedPresets: {},
    }
  },
  computed: {
    ...mapGetters({groups: get.PRESET_GROUPS}),
  },
  async created() {
    await this[action.GET_PRESETS_GROUPS]()

    this.groups.forEach((group) => {
      this.selectedPresets[group.id] = []

      const presetsIds = group.presets.map(({id}) => id)

      this.selectedPresets[group.id] = this.projectPresets.filter((item) =>
        presetsIds.includes(item)
      )
    })
  },
  methods: {
    ...mapActions([action.GET_PRESETS_GROUPS, action.UPDATE_PRESET]),
    openSaveAsModal() {
      this.isOpenSaveAsModal = true
    },
    async updatePreset() {
      if (this.editablePreset) {
        await this[action.UPDATE_PRESET]({
          presetId: this.activePreset,
          data: {query: this.expertQuery},
        })

        this.editablePreset = false
      } else {
        this.openSaveAsModal()
      }
    },
    async changeExpertQuery(query) {
      this.isShowExpertInput = false
      this.expertQuery = query
      await nextTick()
      this.isShowExpertInput = true
    },
    isGroupChecked(isChecked, groupId, presets) {
      if (!isChecked) {
        this.selectedPresets[groupId] = []
        return
      }

      presets.forEach(({id}) => this.selectedPresets[groupId].push(id))
    },
    addFilterToProject() {
      this.$emit(
        'add-expert-filter',
        Object.values(this.selectedPresets).flat()
      )
    },
    editPreset(preset) {
      this.editablePreset = true
      this.activePreset = preset.id
      this.changeExpertQuery(preset.query)
    },
    resetQuery() {
      this.activePreset = false
      this.changeExpertQuery([''])
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;

  width: 75vw;
}

.expert-filter-section {
  width: 100%;
  padding: 24px;

  background-color: var(--background-secondary-color);
}

.expert-filter-buttons {
  display: flex;
  justify-content: flex-end;

  gap: 16px;
  margin-top: 24px;

  .reset-icon {
    transform: rotate(45deg);
  }
}

.presets-section {
  width: 100%;
  padding: 24px;

  background-color: var(--background-primary-color);
  border-left: var(--border-primary);
}

.preset-label {
  margin-bottom: 8px;

  color: var(--typography-title-color);
}

.edit-preset-btn {
  cursor: pointer;

  border: none;
  background-color: transparent;
}

.active-preset {
  border: 1px solid var(--border-active-color);
  border-radius: var(--border-radius);
  background-color: var(--primary-active-color);
}

.preset-groups {
  display: flex;
  flex-direction: column;

  padding: 8px;
  height: 265px;

  background-color: var(--background-secondary-color);
  border-radius: var(--border-radius);

  li {
    display: flex;
    align-items: center;

    gap: 10px;
    padding: 8px 12px;

    list-style-type: none;
  }

  .group {
    font-size: 16px;
    font-weight: 500;

    span {
      flex-grow: 1;
    }
  }

  .preset {
    span {
      flex-grow: 1;
    }
  }
}

.mb {
  margin-bottom: 10px;
}

.footer {
  display: flex;
  justify-content: flex-end;

  width: 100%;
  padding: 18px 24px;
  gap: 16px;

  background-color: var(--background-secondary-color);
  border-top: var(--border-primary);
}
</style>
