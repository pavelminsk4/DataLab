<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Expert filter</span>
    </template>

    <div class="wrapper">
      <section class="expert-filter-section">
        <ExpertField v-model="expValue" label="Filter query" />

        <div class="expert-filter-buttons">
          <BaseButton :is-not-background="true">
            Detailed search syntax
          </BaseButton>
          <BaseButton :is-not-background="true">Reset</BaseButton>
        </div>
      </section>
      <section class="presets-section">
        <div class="preset-label">Presets</div>
        <div>
          <BaseInput v-model="searchPreset" />

          <ul class="preset-groups">
            <template
              v-for="{id: groupId, name, presets} in groups"
              :key="groupId"
            >
              <li class="group" @click="isOpenGroup[name] = !isOpenGroup[name]">
                <BaseCheckbox />
                <span>{{ name }}</span>

                <ArrowheadIcon
                  :direction="isOpenGroup[name] ? 'top' : 'down'"
                />
              </li>
              <template v-if="isOpenGroup[name]">
                <li
                  v-for="(preset, index) in presets"
                  :key="preset.id"
                  :class="['preset', index + 1 === presets.length && 'mb']"
                >
                  <BaseCheckbox />
                  <span>{{ preset.name }}</span>
                  <EditIcon />
                </li>
              </template>
            </template>
          </ul>
        </div>
      </section>
    </div>

    <footer class="footer">
      <BaseButton :is-not-background="true">Save as</BaseButton>
      <BaseButton :is-not-background="true">Save</BaseButton>
      <BaseButton :is-not-background="true">Add Filter</BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'
import ExpertField from '@components/expert-filter/ExpertField'
import BaseInput from '@components/common/BaseInput'
import BaseCheckbox from '@/components/BaseCheckbox2'
import ArrowheadIcon from '@components/icons/ArrowheadIcon'
import EditIcon from '@/components/icons/EditIcon'

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
  },
  data() {
    return {
      expValue: '',
      searchPreset: '',
      isOpenGroup: {},
    }
  },
  created() {
    this.groups = [
      {
        id: 1,
        name: 'Gr1',
        presets: [
          {
            name: 'preset 1',
            id: 423,
            query_filter: 'Elon AND CAT',
          },

          {
            name: 'preset 2',
            id: 413,
            query_filter: '(Elon AND Cat) OR Dog',
          },
        ],
      },
      {
        id: 12,
        name: 'Gr12',
        presets: [
          {
            name: 'preset 1',
            id: 423,
            query_filter: 'Elon AND CAT',
          },

          {
            name: 'preset 2',
            id: 413,
            query_filter: '(Elon AND Cat) OR Dog',
          },
        ],
      },
      {
        id: 13,
        name: 'Gr13',
        presets: [
          {
            name: 'preset 1',
            id: 423,
            query_filter: 'Elon AND CAT',
          },

          {
            name: 'preset 2',
            id: 413,
            query_filter: '(Elon AND Cat) OR Dog',
          },
        ],
      },
    ]
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

.preset-groups {
  display: flex;
  flex-direction: column;
  padding: 8px;

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
