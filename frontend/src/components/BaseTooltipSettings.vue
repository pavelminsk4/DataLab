<template>
  <div class="settings-container" ref="settings-wrapper">
    <div v-if="isOpenSettings" class="options-container">
      <slot></slot>
    </div>
    <PointsIcon
      :class="['points-icon', isOpenSettings && 'active-points']"
      @click.stop="openSettings"
    />
  </div>
</template>

<script>
import PointsIcon from '@/components/icons/PointsIcon'

export default {
  name: 'BaseTooltipSettings',
  components: {
    PointsIcon,
  },
  props: {
    id: {
      type: [Number, String],
      default: '',
    },
  },
  data() {
    return {
      isOpenSettings: false,
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    openSettings() {
      this.isOpenSettings = !this.isOpenSettings
    },
    close() {
      const elements = document.querySelectorAll('.settings-container')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this.isOpenSettings = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-container {
  position: relative;

  width: 30px;
  height: 30px;
}

.options-container {
  position: absolute;
  right: 40px;

  display: flex;
  flex-direction: column;

  white-space: nowrap;

  border-radius: 4px;
  padding: 10px 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.22);

  background: var(--primary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 110%;
  color: var(--secondary-button-color);

  &::after {
    content: '';

    position: absolute;
    top: 29%;
    right: -10px;

    transform: translate(-50%, -50%) rotate(225deg);

    margin-left: 2px;

    border-width: 5px;
    border-style: solid;
    border-bottom-left-radius: 2px;

    color: var(--primary-text-color);
  }
}

.close-options {
  display: none;
}

.points-icon {
  z-index: 3;

  flex-shrink: 0;

  width: 30px;
  height: 30px;

  transition: all 0.3s;
  pointer-events: stroke;

  color: var(--secondary-text-color);
}

.points-icon:hover {
  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--button-primary-color);
}

.active-points {
  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--button-primary-color);
}
</style>
